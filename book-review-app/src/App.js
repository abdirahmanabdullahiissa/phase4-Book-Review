import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import BookList from './components/BookList';
import BookDetails from './components/BookDetails';
import SubmitBook from './components/SuggestBook';
import ReviewForm from './components/ReviewForm';
import CommunityForum from './components/CommunityForum';
import PostForm from './components/PostForm';

const App = () => {
  return (
    <Router>
      <Routes>
        <Route exact path="/">
          <BookList />
        </Route>
        <Route path="/book/:id">
          <BookDetails />
        </Route>
        <Route path="/submit-book">
          <SubmitBook />
        </Route>
        <Route path="/review/:bookId">
          <ReviewForm />
        </Route>
        <Route exact path="/forum">
          <CommunityForum />
        </Route>
        <Route path="/create-post">
          <PostForm />
        </Route>
      </Routes>
    </Router>
  );
};

export default App;