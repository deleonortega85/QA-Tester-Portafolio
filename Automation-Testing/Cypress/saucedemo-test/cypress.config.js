const { defineConfig } = require("Cypress");

module.exports = defineConfig({
  //reporter: 'cypress-mochawesome-reporter',
  e2e: {
    //video:true,
    setupNodeEvents(on, config) {    
      //require('cypress-mochawesome-reporter/plugin')(on);
    },
    baseUrl:'https://www.saucedemo.com'
  },
});
