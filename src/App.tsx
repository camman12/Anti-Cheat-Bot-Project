import CssBaseline from '@material-ui/core/CssBaseline';
import Header from './Header';
import Admin from './Admin';

function App() {
  return (
    <div className="App">
      <CssBaseline />

      <Header title="Anti-Cheat Project" />
      <Admin />
    </div>
  );
}

export default App;
