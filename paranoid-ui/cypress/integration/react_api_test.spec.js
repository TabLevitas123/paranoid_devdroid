
describe('React-API Integration Test', () => {
  it('should load the React app and display API data', () => {
    cy.visit('/');
    cy.get('body').contains('Hello from Flask API!');
  });
});
