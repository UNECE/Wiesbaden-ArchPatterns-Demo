import clone from "lodash.clone";

/*
 Aggregates questionnaire to produce a summary.
 Initialized with starting values.
*/
let finalProduct = {
  totalNumberOfRespondents: 0,
  totalNumberOfChildren: 0,
  professions: []
};

const process = questionnaire => {
  console.log("Processing questionnaire", questionnaire);
  // Update the product
  let newProduct = clone(finalProduct);
  newProduct.totalNumberOfRespondents = newProduct.totalNumberOfRespondents + 1;
  newProduct.totalNumberOfChildren = parseInt(
    questionnaire.children
  );
  // Store
  finalProduct = newProduct;
  console.log("Update final product", newProduct);
  return newProduct;
};

export default process;
