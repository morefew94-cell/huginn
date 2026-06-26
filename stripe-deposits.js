/**
 * Stripe checkout — Price IDs are server-side only (Vercel env vars).
 * Reference: vercel-env-deposits.example
 */
window.HUGINN_CHECKOUT = {
  starter: '/api/checkout?tier=starter',
  growth: '/api/checkout?tier=growth',
  pro: '/api/checkout?tier=pro',
  changeWindow: '/api/checkout?tier=changeWindow',
};

document.querySelectorAll('[data-stripe-deposit]').forEach((el) => {
  const tier = el.getAttribute('data-stripe-deposit');
  const url = window.HUGINN_CHECKOUT[tier];
  if (url) el.href = url;
});
