/**
 * Replace REPLACE_* URLs with live Stripe Payment Link URLs.
 * Deposits: Starter $20 · Growth $50 · Pro $100
 * Change window (post-finalisation, no care plan): $99 for 10 business days
 */
window.HUGINN_STRIPE_DEPOSITS = {
  starter: 'https://buy.stripe.com/REPLACE_STARTER_DEPOSIT_20',
  growth: 'https://buy.stripe.com/REPLACE_GROWTH_DEPOSIT_50',
  pro: 'https://buy.stripe.com/REPLACE_PRO_DEPOSIT_100',
  changeWindow: 'https://buy.stripe.com/REPLACE_CHANGE_WINDOW_99',
};
