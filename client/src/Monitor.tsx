import Box from '@material-ui/core/Box';
import Container from '@material-ui/core/Container';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';

// TODO: Fetch from server
let eventLog = [
  'Bot found cheating material at https://quizlet.com/321920987/cs370-all-quizzes-flash-cards/. Site has been reported.',
  'Bot found cheating material at https://quizlet.com/300199345/cs-344-flash-cards/. Site has been reported.',
  'Bot found cheating material at https://quizlet.com/142666571/cs-325-final-exam-flash-cards/. Site has been reported.',
  'Bot found cheating material at https://quizlet.com/205802391/cs490-flash-cards/. Site has been reported.',
];

eventLog = [...eventLog, ...eventLog, ...eventLog];

export default function Monitor() {
  return (
    <Box paddingTop={2}>
      <Container maxWidth="lg">
        <List>
          {eventLog.map((event, i) => (
            <ListItem button key={i}>
              <ListItemText primary={event} />
            </ListItem>
          ))}
        </List>
      </Container>
    </Box>
  );
}
