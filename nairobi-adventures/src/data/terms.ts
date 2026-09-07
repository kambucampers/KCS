/**
 * Booking terms shown on the contact, tours and tour pages.
 *
 * These are the operator's standard terms. Editing them here updates every page
 * that quotes them, so the site never states two different policies.
 */
export const terms = {
  responseTime: 'within one working day',
  deposit: '30 percent of the total to confirm the date',
  balance: 'the balance on the morning of the tour, before departure',
  paymentMethods: 'bank transfer, M-Pesa, or cash in US dollars or Kenyan shillings on the day',
  cancellation: {
    free: 'more than 7 days before the tour, the deposit is refunded in full',
    partial: 'between 3 and 7 days before, half the total is refunded',
    none: 'inside 72 hours, the booking is not refundable, because the vehicle and the park booking are already committed',
    operator:
      'if Nairobi Adventures cancels, or a flight delay makes a layover tour unsafe against your check-in time, you are refunded in full',
  },
  bookingLeadTime:
    'as early as you can when the day includes the elephant orphanage, because its single daily visiting window is booked in advance and sells out in high season',
} as const;
