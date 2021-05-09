import { MouseEvent } from 'react';
import { useHistory, Link } from 'react-router-dom';
import { makeStyles } from '@material-ui/core/styles';
import Drawer, { DrawerProps } from '@material-ui/core/Drawer';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import LockIcon from '@material-ui/icons/Lock';
import ExitToAppIcon from '@material-ui/icons/ExitToApp';
import HomeIcon from '@material-ui/icons/Home';
import ListIcon from '@material-ui/icons/List';
import { isLoggedIn, logout } from './auth';

const useStyles = makeStyles({
  list: {
    width: 250,
  },
});

interface Props {
  onListClick?: (event: MouseEvent) => void;
}

export default function Sidenav({ onListClick, ...props }: Props & DrawerProps) {
  const classes = useStyles();
  const history = useHistory();

  const handleLogout = () => {
    logout();
    history.push('/login');
  };

  return (
    <Drawer anchor="left" {...props}>
      <List className={classes.list} onClick={onListClick}>
        <ListItem button component={Link} to="/">
          <ListItemIcon><HomeIcon /></ListItemIcon>
          <ListItemText primary="Admin" />
        </ListItem>

        <ListItem button component={Link} to="/monitor">
          <ListItemIcon><ListIcon /></ListItemIcon>
          <ListItemText primary="Monitor" />
        </ListItem>

        {!isLoggedIn() ?
          <ListItem button component={Link} to="/login">
            <ListItemIcon><LockIcon /></ListItemIcon>
            <ListItemText primary="Login" />
          </ListItem>
        : <ListItem button onClick={handleLogout}>
            <ListItemIcon><ExitToAppIcon /></ListItemIcon>
            <ListItemText primary="Logout" />
          </ListItem>
        }
      </List>
    </Drawer>
  );
}
