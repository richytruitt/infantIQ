import React, { useState, useEffect } from 'react';
import ReactDOM from 'react-dom/client';
import Col from 'react-bootstrap/Col';
import Container from 'react-bootstrap/Container';
import Image from 'react-bootstrap/Image';
import Row from 'react-bootstrap/Row';

import 'bootstrap/dist/css/bootstrap.min.css';

// React Chart Component
import { AgCharts } from 'ag-charts-react';

function Data(props){
    const [data, setData] = useState([]);


    useEffect(() => {
         fetch('https://dzzr74ct51.execute-api.us-east-1.amazonaws.com/LambdaAPIGatewayDeployment/api/getData')
          .then(response => response.json())
          .then(json => setData(json["data"]))
          .catch(error => console.error(error));
      }, []);

    
    const totals_options_bar = {
        "data":[
            {"action": "nap", "total": data.filter((obj) => obj.action === "nap").length},
            {"action": "feeding", "total": data.filter((obj) => obj.action === "feeding").length},
            {"action": "diaper_change", "total": data.filter((obj) => obj.action === "diaper_change").length}
        ],
        "series": [{ type: 'bar', xKey: 'action', yKey: 'total' }],
        
    };

    const totals_options_pie = {
        "data":[
            {"action": "nap", "total": data.filter((obj) => obj.action === "nap").length},
            {"action": "feeding", "total": data.filter((obj) => obj.action === "feeding").length},
            {"action": "diaper_change", "total": data.filter((obj) => obj.action === "diaper_change").length}
        ],
        series: [{ type: 'pie', angleKey: 'total', legendItemKey: 'action' }],
        
    };


    return (
        <div>
            {/* <table>
                <tbody>
                {data && (data.map(index => 
                <tr key={index.timestamp}>
                <td>{index.timestamp}</td>
                <td>{index.action}</td>
                </tr>))}
                </tbody>

            </table> */}
            <Container>
                <Row>
                <Col xs={6} md={6}>
                    <AgCharts options={totals_options_bar} />
                 </Col>
                 <Col xs={6} md={6}>
                    <AgCharts options={totals_options_pie} />
                 </Col>
                </Row>
            </Container>

        </div>
    );
}
export default Data