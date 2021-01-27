import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Link from '@material-ui/core/Link';
import Typography from '@material-ui/core/Typography';

interface Props {
  title: string;
}

export default function Header({ title }: Props) {
  return (
    <AppBar position="static">
      <Toolbar>
        <Link href="#" color="inherit">
          <Typography variant="h6">
            {title}
          </Typography>
        </Link>
      </Toolbar>
    </AppBar>
  );
}
