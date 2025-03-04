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
    // Editing the div's style
    humanMsg.style.backgroundColor = "lightblue";  
    humanMsg.style.borderRadius = "15px";         
    humanMsg.style.alignSelf = "flex-end"; 
    humanMsg.style.width = "fit-content"; 
    humanMsg.style.minHeight = "20px"  
    humanMsg.style.marginBottom = "16px";
    humanMsg.style.padding = "10px 20px 10px 20px"  
    // Adding the div to the conversation
    conversation.appendChild(humanMsg);

    console.log("Message:", formData.get("message-box"));
    let textarea = document.getElementById("msg-box");
    textarea.value = ""; // Removing all the text in the text area
});