const TIER_ENV_KEYS = {
  starter: 'HUGINN_STRIPE_PRICE_STARTER_DEPOSIT',
  growth: 'HUGINN_STRIPE_PRICE_GROWTH_DEPOSIT',
  pro: 'HUGINN_STRIPE_PRICE_PRO_DEPOSIT',
  changeWindow: 'HUGINN_STRIPE_PRICE_CHANGE_WINDOW',
};

function siteOrigin(req) {
  const proto = req.headers['x-forwarded-proto'] || 'https';
  const host = req.headers['x-forwarded-host'] || req.headers.host || 'www.huginnweb.com';
  return `${proto}://${host}`;
}

module.exports = async (req, res) => {
  if (req.method !== 'GET') {
    res.status(405).json({ error: 'Method not allowed' });
    return;
  }

  const tier = req.query.tier;
  const envKey = TIER_ENV_KEYS[tier];
  if (!envKey) {
    res.status(400).json({ error: 'Invalid tier' });
    return;
  }

  const priceId = process.env[envKey];
  const secretKey = process.env.STRIPE_SECRET_KEY;
  if (!priceId || !secretKey) {
    res.status(500).json({ error: 'Checkout not configured' });
    return;
  }

  const origin = siteOrigin(req);
  const params = new URLSearchParams({
    mode: 'payment',
    'line_items[0][price]': priceId,
    'line_items[0][quantity]': '1',
    success_url: `${origin}/thank-you`,
    cancel_url: `${origin}/#packages`,
  });

  const stripeRes = await fetch('https://api.stripe.com/v1/checkout/sessions', {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${secretKey}`,
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: params.toString(),
  });

  const session = await stripeRes.json();
  if (!stripeRes.ok) {
    console.error('Stripe checkout error:', session);
    res.status(500).json({ error: 'Could not create checkout session' });
    return;
  }

  res.redirect(303, session.url);
};
