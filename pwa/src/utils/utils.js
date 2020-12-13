import { uuid } from "uuidv4";
const { default: Axios } = require("axios");

export const config = {
    url : "https://api-hml.paysmart.com.br/paySmart/ps-processadora/v1/",
    api_key : "c127b101d415dd35fa55e5721e891deb4ef3ee3f",
    produtoPF : "086001",
    produtoPJ : "086002"
}

export const axiosAuta = Axios.create({
    baseURL: "https://api-hml.paysmart.com.br/paySmart/ps-processadora/v1/",
    headers: {
        "API-Key" : config.api_key,
        "IdempotencyKey" : uuid(),
        "accept" : "application/json",
        "Content-Type" : "application/json"
    }
});

var createAccount = (newAccount) => {
    
}