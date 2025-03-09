let countMsgAI = 0;
let countMsgHuman = 0;

// Handling user submission of a response
document.getElementById("msg-form").addEventListener("submit", async function(event) {
    event.preventDefault();
    let formData = new FormData(this);

    // Putting the chat message into a new div
    let humanMsg = document.createElement("div");
    let conversation = document.getElementById("conversation");
    humanMsg.textContent = formData.get("message-box");
    humanMsg.className += "conversation-text"
    // Adding the div to the conversation
    conversation.appendChild(humanMsg);

    console.log("Message:", formData.get("message-box"));
    let textarea = document.getElementById("msg-box");
    textarea.value = ""; // Removing all the text in the text area

    sendData()
});

// Getting the AI's response after the User sends a message
function sendData() {
    // Getting all the messages in conversation-text class
    let texts = document.getElementsByClassName('conversation-text');
    let textsString = "";
    for (let message of texts) {
        textsString += "\nUser:" + message.textContent;
    }
    console.log(textsString);

    fetch('http://127.0.0.1:1000/conversation', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ conversation: textsString }),
    })
    .then(response => response.json())
    .then(data => {
       console.log(data.response);
    })
    .catch((error) => {
        console.log('Error:', error);
    });
}