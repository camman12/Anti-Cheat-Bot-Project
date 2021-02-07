import { makeStyles } from '@material-ui/core/styles';
import Drawer, { DrawerProps } from '@material-ui/core/Drawer';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import HomeIcon from '@material-ui/icons/Home';

const useStyles = makeStyles({
  list: {
    width: 250,
  },
});

export default function Sidenav(props: DrawerProps) {
  const classes = useStyles();

  return (
    <Drawer anchor="left" {...props}>
      <List className={classes.list}>
        <ListItem button>
          <ListItemIcon><HomeIcon /></ListItemIcon>
          <ListItemText primary="Admin" />
        </ListItem>
      </List>
    </Drawer>
  );
}
