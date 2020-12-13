import React from "react";
import { Card, CardBody, CardTitle, CardSubtitle } from "shards-react";

export default class Cartao extends React.Component {
    render() {
        return (
            <Card>
              <CardBody>
                <CardTitle>{this.props.titular}</CardTitle>
                <CardSubtitle>{this.props.numero}</CardSubtitle>
                {this.props.validade}
              </CardBody>
            </Card>
          );
    }
}