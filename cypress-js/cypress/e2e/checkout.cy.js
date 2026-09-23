describe('Cart flow', () => {
  beforeEach(() => {
    cy.visit('/')
    cy.get('#user-name').type('standard_user')
    cy.get('#password').type('secret_sauce')
    cy.get('#login-button').click()
  })

  it('adds item to cart', () => {
    cy.get('button[data-test^="add-to-cart"]').first().click()
    cy.get('.shopping_cart_badge').should('have.text', '1')
  })

  it('shows 6 products', () => {
    cy.get('.inventory_item').should('have.length', 6)
  })
})