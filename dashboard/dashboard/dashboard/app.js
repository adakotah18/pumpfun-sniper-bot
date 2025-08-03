document.addEventListener("DOMContentLoaded", () => {
    const app = document.getElementById("app");
    app.innerHTML = `
        <p>PnL: $0</p>
        <p>Win Rate: 90%</p>
        <p>Front‑Run Advantage: 113ms</p>
        <p>Wallet: Phantom (SOL) — Active</p>
        <button onclick="alert('Rotating Wallet...')">Rotate Wallet Now</button>
    `;
});
