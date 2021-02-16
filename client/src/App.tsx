import {
  BrowserRouter as Router,
  Switch,
  Route,
} from 'react-router-dom';
import CssBaseline from '@material-ui/core/CssBaseline';
import Header from './Header';
import Admin from './Admin';

function App() {
  return (
    <div className="App">
      <CssBaseline />

      <Router>
        <Header title="Anti-Cheat Project" />

        <Switch>
          <Route path="/">
            <Admin />
          </Route>
        </Switch>
      </Router>
    </div>
  );
}

export default App;
