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
    //humanMsg.className += "human-text";
    humanMsg.classList.add("conversation-text", "human-text");
    // Adding the div to the conversation
    conversation.appendChild(humanMsg);

    console.log("Message:", formData.get("message-box"));
    let textarea = document.getElementById("msg-box");
    textarea.value = ""; // Removing all the text in the text area

    // Getting all the past messages
    let texts = document.getElementsByClassName('conversation-text');
    let textsString = "";
    for (let message of texts) {
        textsString += "\nUser:" + message.textContent;
    }
    if (texts.length >= 4) {
        console.log("Time to evaluate")
        // Making the final message a converstion closer
        let finalMsg = document.createElement("div");
        let conversation = document.getElementById("conversation");
        finalMsg.textContent = data.response;
        aiMsg.classList.add("conversation-text", "ai-text");
    }
    // Sending it and getting the response if there aren't too many messages
    sendData(textsString)
});

// Getting the AI's response after the User sends a message
async function sendData() {
    try {
        let response = await fetch('http://127.0.0.1:1000/conversation', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ conversation: textsString }),
        });

        let data = await response.json(); // Wait for JSON parsing
        console.log(data.response);
        // Putting the response message into a new div
        let aiMsg = document.createElement("div");
        let conversation = document.getElementById("conversation");
        aiMsg.textContent = data.response;
        aiMsg.classList.add("conversation-text", "ai-text");
        // Introducing a 2 second delay before the AI response
        setTimeout(function() {
            // Code to execute after 2 seconds
          }, 2000); // 2000 milliseconds = 2 seconds
          
        // Adding the div to the conversation
        conversation.appendChild(aiMsg);
    } catch (error) {
        console.log('Error:', error);
    }
}
