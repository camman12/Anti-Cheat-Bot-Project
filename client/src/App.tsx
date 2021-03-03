import {
  BrowserRouter as Router,
  Switch,
  Route,
} from 'react-router-dom';
import CssBaseline from '@material-ui/core/CssBaseline';
import { Helmet, HelmetProvider } from 'react-helmet-async';
import Header from './Header';
import Admin from './Admin';
import Login from './Login';

function App() {
  return (
    <HelmetProvider>
      <div className="App">
        <CssBaseline />

        <Helmet>
          <meta charSet="utf-8" />
          <title>Anti-Cheat Project</title>
        </Helmet>

        <Router>
          <Header title="Anti-Cheat Project" />

          <Switch>
            <Route path="/login">
              <Login />
            </Route>

            <Route path="/">
              <Admin />
            </Route>
          </Switch>
        </Router>
      </div>
    </HelmetProvider>
  );
}

export default App;
