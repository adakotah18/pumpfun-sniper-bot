export default function Dashboard() {
  return (
    <div style={{ fontFamily: 'Arial, sans-serif', padding: '20px' }}>
      <h1>Dashboard: PnL Graph, Wallet Rotation, DRY_RUN Mode Enabled</h1>

      <div style={{ marginTop: '20px' }}>
        <p><strong>PnL:</strong> $0</p>
        <p><strong>Win Rate:</strong> 90%</p>
        <p><strong>Front‑Run Advantage:</strong> 113ms</p>
        <p><strong>Wallet:</strong> Phantom (SOL) — Active</p>
        <button style={{ marginTop: '10px', padding: '8px 12px' }}>Rotate Wallet Now</button>
      </div>

      <div style={{ marginTop: '30px' }}>
        <h2>Trade History</h2>
        <table border="1" cellPadding="5">
          <thead>
            <tr>
              <th>Token</th>
              <th>Action</th>
              <th>PnL</th>
              <th>Timestamp</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>MEME123</td>
              <td>BUY</td>
              <td>+100%</td>
              <td>2025-08-01 12:32</td>
            </tr>
            <tr>
              <td>DOGE999</td>
              <td>SELL</td>
              <td>+100%</td>
              <td>2025-08-02 14:35</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  );
}
