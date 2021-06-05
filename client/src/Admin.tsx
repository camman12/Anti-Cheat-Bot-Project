import { useState, useEffect } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';
import Grid from '@material-ui/core/Grid';
import TextField from '@material-ui/core/TextField';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';
import MenuItem from '@material-ui/core/MenuItem';
import Select from '@material-ui/core/Select';
import FormControl from '@material-ui/core/FormControl';
import InputLabel from '@material-ui/core/InputLabel';
import IconButton from '@material-ui/core/IconButton';
import CloseIcon from '@material-ui/icons/Close';
import Typography from '@material-ui/core/Typography';
import Box from '@material-ui/core/Box';

const useStyles = makeStyles({
  root: {
    marginTop: 10,
  },
  section: {
    display: 'inline-block',
    width: '50%',
    padding: 20,
  },
});

async function fetchKeywords() {
  const res = await fetch('/api/keywords', {
    headers: {
      'Authorization': `Bearer ${localStorage.getItem('token') as any}`,
    },
  });

  const body = await res.json();
  return body.keywords;
}

async function uploadKeyword(keyword: string) {
  const res = await fetch('/api/keyword', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${localStorage.getItem('token') as any}`,
    },
    body: JSON.stringify({ keyword }),
  });
}

async function deleteKeyword(keyword: string) {
  const res = await fetch('/api/keyword/delete', {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${localStorage.getItem('token') as any}`,
    },
    body: JSON.stringify({ keyword }),
  });
}

export default function Admin() {
  const classes = useStyles();
  const [keywordInput, setKeywordInput] = useState('');
  const [keywords, setKeywords] = useState([] as string[]);

  useEffect(() => {
    async function set() {
      const k = await fetchKeywords();
      setKeywords(k);
    }

    set();
  }, []);

  const handleChange = (e: any) => {
    setKeywordInput(e.target.value);
  };

  const handleKeyDown = (e: any) => {
    if (e.key === 'Enter') {
      const newKeywords = [...keywords, e.target.value];
      setKeywords(newKeywords);
      setKeywordInput('');

      uploadKeyword(e.target.value);
    }
  };

  const [freq, setFreq] = useState(0);

  const handleFreqChange = (e: any) => {
    setFreq(e.target.value);
  };

  const handleDeleteKeyword = (index: number) => {
    const newKeywords = [...keywords];
    const deleted = newKeywords.splice(index, 1);
    setKeywords(newKeywords);

    deleteKeyword(deleted[0]);
  };

  return (
    <Container maxWidth="lg">
      <Box marginBottom={1} marginTop={1}>
          <Typography variant="h2">User configuration</Typography>
      </Box>
      <Grid container spacing={3} className={classes.root}>
        <Grid item xs={6}>
          <TextField
            label="Add keyword"
            value={keywordInput}
            onChange={handleChange}
            onKeyDown={handleKeyDown}
            fullWidth
          />

          <List>
            {keywords.map((keyword, i) => (
              <ListItem button key={i}>
                <ListItemText primary={keyword} />
                <IconButton onClick={() => handleDeleteKeyword(i)}>
                  <CloseIcon />
                </IconButton>
              </ListItem>
            ))}
          </List>
        </Grid>

        <Grid item xs={6}>
          <FormControl fullWidth>
            <InputLabel>Notification Frequency</InputLabel>
            <Select
              value={freq}
              onChange={handleFreqChange}
            >
              <MenuItem value={0}>Immediately</MenuItem>
              <MenuItem value={1}>Hourly</MenuItem>
              <MenuItem value={2}>Daily</MenuItem>
              <MenuItem value={3}>Weekly</MenuItem>
            </Select>
          </FormControl>
        </Grid>
      </Grid>
    </Container>
  );
}
