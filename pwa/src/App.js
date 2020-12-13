import React from "react";
import './App.css';
import Menu from './components/Menu';
import Cartao from './components/Cartao';
import { 
  Button, 
  Container,
  Row, 
  Col
} from 'shards-react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faMoneyBill, faMoneyBillAlt } from '@fortawesome/free-solid-svg-icons';
import NovaConta from "./components/NovaConta";

export default class App extends React.Component {
  
  render() {
    return (
      <>
      <Menu/>
      <Container style={{marginTop: 15}}>
        <Cartao
        titular="Alexandre Werneck"
        numero="0000.0000.0000.0000"
        validade="05/2022"
        />
        <div style={{marginTop: 15}}>
        <Row style={{flex: 1, flexDirection: 'row'}}>
          <Col>
            <Button theme="light" style={{marginLeft: 5}}>
              <FontAwesomeIcon icon={faMoneyBill} />
              Transferir
            </Button>
            <Button theme="light">
              <FontAwesomeIcon icon={faMoneyBillAlt} />
              Pagar
            </Button>
            <Button theme="light">
              <FontAwesomeIcon icon={faMoneyBill} />
              Saque
            </Button>
            <Button theme="light"
            onClick={() => this.criarCartao()}
            >
              <FontAwesomeIcon icon={faMoneyBill} />
              t
            </Button>
          </Col>
        </Row>
        </div>
      </Container>
    </>
    )
  }
}
