import React from "react";
import { Card, CardBody, 
    Form, FormInput, FormGroup ,
    Button
} from "shards-react";
import { axiosAuta, config, fetchAuta } from "../utils/utils";

export default class NovaConta extends React.Component {

    newAccount = () => {
        var newAccountData = {
            "psProductCode": config.produtoPF,
            "accountOwner": {
                "fullName": "Alexandre Werneck",
                "identityDocumentNumber": "07602777610",
                "contactInformation": { "personalPhoneNumber1": "+5521987009793",  "email": "xanwerneck@gmail.com" }
            },
            "billingAddress": {
                "addressLine1": "R. Manoelito de Ornellas",
                "addressLine2": "55",
                "city": "Porto Alegre",
                "state": "RS",
                "neighborhood": "Praia de Belas",
                "zipcode": "990000"
            },
            "cardDeliveryAddress": {
                "addressLine1": "R. Manoelito de Ornellas",
                "addressLine2": "55",
                "city": "Porto Alegre",
                "state": "RS",
                "neighborhood": "Praia de Belas",
                "zipcode": "990000"
            }
        }

        axiosAuta.post('accounts', newAccountData)
        .then(res => res.json())
        .then(res => console.log(res))
    }
    render() {
        return (
            <Card>
              <CardBody>
                <Form>
                    <FormGroup>
                        <label htmlFor="#username">Username</label>
                        <FormInput id="#username" placeholder="Username" />
                    </FormGroup>
                    <FormGroup>
                        <label htmlFor="#password">Password</label>
                        <FormInput type="password" id="#password" placeholder="Password" />
                    </FormGroup>
                </Form>
                <Button 
                onClick={() => this.newAccount()}
                block fill them="light">
                    Enviar
                </Button>
              </CardBody>
            </Card>
          );
    }
}