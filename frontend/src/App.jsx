/**
 * Root application component
 * Only routing and providers live here
 */
import { BrowserRouter } from "react-router-dom";

function App() {
  return (
    <BrowserRouter>
      <div className="min-h-screen bg-gray-50">
        FinWise Frontend Running
      </div>
    </BrowserRouter>
  );
}

export default App;
