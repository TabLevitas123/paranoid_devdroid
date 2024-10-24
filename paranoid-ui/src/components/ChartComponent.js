
import React, { useState, useEffect, useRef } from 'react';
import { Line } from 'react-chartjs-2';
import { Chart as ChartJS } from 'chart.js/auto';
import './ChartComponent.css';

const ChartComponent = () => {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const chartRef = useRef(null);

  useEffect(() => {
    const ws = new WebSocket('wss://example-websocket-server.com/socket');

    ws.onmessage = (event) => {
      const message = JSON.parse(event.data);
      setData((prevData) => [...prevData, message.value]);
      setLoading(false);  // Stop spinner when data is received
    };

    return () => {
      ws.close();
    };
  }, []);

  const chartData = {
    labels: data.map((_, index) => `Data ${index + 1}`),
    datasets: [
      {
        label: 'Real-Time Data',
        data: data,
        borderColor: 'rgba(75, 192, 192, 1)',
        borderWidth: 2,
        fill: false,
      },
    ],
  };

  const chartOptions = {
    scales: {
      y: {
        beginAtZero: true,
      },
    },
  };

  return (
    <div className="chart-container">
      <h2>Real-Time Data Visualization</h2>
      {loading ? (
        <div className="spinner">Loading...</div>  // Spinner during loading
      ) : (
        <Line ref={chartRef} data={chartData} options={chartOptions} />
      )}
    </div>
  );
};

export default ChartComponent;
