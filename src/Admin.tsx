import { useState } from 'react';
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

export default function Admin() {
  const classes = useStyles();
  const [keywordInput, setKeywordInput] = useState('');
  const [keywords, setKeywords] = useState([] as string[]);

  const handleChange = (e: any) => {
    setKeywordInput(e.target.value);
  };

  const handleKeyDown = (e: any) => {
    if (e.key === 'Enter') {
      const newKeywords = [...keywords, e.target.value];
      setKeywords(newKeywords);
      setKeywordInput('');
    }
  };

  const [freq, setFreq] = useState(0);

  const handleFreqChange = (e: any) => {
    setFreq(e.target.value);
  };

  return (
    <Container maxWidth="lg">
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
