# BUG-002: Cart badge does not persist across session

**Severity:** Low  
**Priority:** P3  
**Status:** Open  
**Environment:** Chrome 120, saucedemo.com

## Steps to Reproduce

1. Login as standard_user
2. Add 1 item to cart
3. Logout
4. Login again

## Expected

Cart state cleared on logout (per spec).

## Actual

Badge shows previous count briefly before refresh.

## Impact

Cosmetic only; no data loss. Automated check added to Cypress `checkout.cy.js`.
