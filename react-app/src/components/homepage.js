import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ChatHome = () => {
  const [messages, setMessages] = useState([]);
  const [friends, setFriends] = useState([]);
  const [friendid, setFriendid] = useState(8);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/app/chat/');
        setFriends(response.data);
        console.log(response.data);
      } catch (error) {
        console.error("Error:", error);
      }
    };

    fetchData();
  }, []);
  const sendMessage = async () => {
    let data = {
      friendid,
      messages,
    }
    try{
      const response = await axios.post('http://127.0.0.1:8000/app/chat/', data);
      console.log(response)
    } catch (error) {
      console.log('error sending message')
    }
  }

  return (
    <div className="chat-container">
      <div className="chat-header">
        <h1>Chat App</h1>
      </div>
      <div className="chat-content">
        <div className="friend-list">
          <h2>Friend List</h2>
          <ul>
            {friends.map((friend) => (
              <button onClick={() => setFriendid(friend.friend_id)} key={friend.friend_id}>
                {friend.friend_name}
              </button>
            ))}
          </ul>
        </div>
        <div>
        <div className="chat-messages">

{friendid === '' ? (
  null
) : (
  <>
    {friends.map((friend) => {
      if (friend.friend_id === parseInt(friendid)) {
        const combinedMessages = [];

        for (let i = 0; i < Math.max(friend.friendmessage.length, friend.usermessage.length); i++) {
          if (i < friend.friendmessage.length) {
            combinedMessages.push(friend.friendmessage[i]);
          }

          if (i < friend.usermessage.length) {
            combinedMessages.push(friend.usermessage[i]);
          }
        }

        return combinedMessages.map((message) => (
          <React.Fragment key={message.message_id}>
            <p>{message.message}</p>
          </React.Fragment>
        ));
      }
      return null;
    })}
  </>
)}
</div>

          <div className="chat-input">
            <input
              type="text"
              placeholder="Type your message..."
              value={messages}
              onChange={(e) => setMessages(e.target.value)}
            />
            <button onClick={sendMessage}>Send</button>
          </div>
        </div>
      </div>
      </div>
  );
};

export default ChatHome;
