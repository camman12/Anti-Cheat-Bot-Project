import { useState } from 'react';
import { Link as RouterLink } from 'react-router-dom';
import { createStyles, makeStyles, Theme } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Link from '@material-ui/core/Link';
import Typography from '@material-ui/core/Typography';
import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/icons/Menu';
import Sidenav from './Sidenav';

const useStyles = makeStyles((theme: Theme) =>
  createStyles({
    menuButton: {
      marginRight: theme.spacing(2),
    },
  }),
);

interface Props {
  title: string;
}

export default function Header({ title }: Props) {
  const classes = useStyles();
  const [drawerOpen, setDrawerOpen] = useState(false);

  const handleMenuClick = (e: any) => {
    setDrawerOpen(true);
  };

  const handleMenuClose = (e: any) => {
    setDrawerOpen(false);
  };

  return (
    <>
      <Sidenav
        open={drawerOpen}
        onClose={handleMenuClose}
        onListClick={handleMenuClose}
      />

      <AppBar position="static">
        <Toolbar>
          <IconButton edge="start" className={classes.menuButton} color="inherit" onClick={handleMenuClick}>
            <MenuIcon />
          </IconButton>

          <Link component={RouterLink} to="/" color="inherit">
            <Typography variant="h6">
              {title}
            </Typography>
          </Link>
        </Toolbar>
      </AppBar>
    </>
  );
}
