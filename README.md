# Text-Editor with Advanced feature
Text Editor with Undo/Redo Feature 
Objective 
The objective of this project is to develop a simple text editor that supports basic text editing 
operations like inserting and deleting text, with an Undo and Redo feature. The undo/redo 
mechanism is managed using two stacks to efficiently track and reverse actions. 
Features 
1.  Insert Text  : The user can add text at any position  in the editor. 
2.  Delete Text  : The user can remove selected text from  the editor. 
3.  Undo Last Action  : Reverts the last action, whether  it is an insertion or deletion. 
4.  Redo Last Action  : Restores the last undone action. 
5.  View Current State  : The user can view the current state of the text at any time. 
6.  Clear Text  : Option to clear all text in the editor. 
7.  Find and Replace  : The ability to find specific text within the document and replace it 
with new text. 
Data Structures 
Undo and Redo Mechanism Using Stacks 
●  Undo Stack  : Stores actions as tuples containing the  operation (insert or delete) and the 
text affected. Each time a new action (insert or delete) is performed, it is pushed onto the 
undo stack. 
●  Redo Stack  : When an undo operation is performed, the action is pushed onto the redo 
stack, allowing the user to redo the action if needed. 
Stack Operations: 
●  Push Operation  : Every time an insert or delete action is executed, the operation and 
associated text are pushed onto the undo stack. 
●  Pop Operation  : When undoing an action, the undo stack is popped, and the action is 
reversed. This reversed action is then pushed onto the redo stack. 
Action Types Stored in Stacks 
●  Insert Action  :  ("insert", text)  — Tracks the text that was inserted. 
●  Delete Action  :  ("delete", text)  — Tracks the text that was deleted. 
Functional Requirements 
1.  Insert Text  : 
○  The user can type or paste text into the editor. 
○  The inserted text is stored in the undo stack. 
2.  Delete Text  : 
○  The user can select a portion of text and delete it. 
○  The deleted text is stored in the undo stack for recovery during undo. 
3.  Undo  : 
○  The editor should revert the last insertion or deletion. 
○  For an insertion, the inserted text is removed, and for a deletion, the deleted text 
is restored. 
4.  Redo  : 
○  The editor should reapply the last undone action (insertion or deletion). 
○  The action from the redo stack is executed and added back to the undo stack. 
5.  View Text  : 
○  The current state of the text is displayed. 
6.  Clear Text  : 
○  The entire text content is removed, and the action is stored in the undo stack for 
potential recovery. 
7.  Find and Replace : 
○  The user can search for a specific word or phrase and replace it with new 
content. 
Use Case Diagram 
Actors: 
●  User  : Can perform insert, delete, undo, redo, and other editing actions. 
Use Cases: 
1.  Insert Text 
2.  Delete Text 
3.  Undo Action 
4.  Redo Action 
5.  View Text 
6.  Clear Text 
7.  Find and Replace 
Non-Functional Requirements 
1.  Performance  : The editor should handle moderate-sized  text files efficiently. Stack 
operations (push/pop) should be constant time. 
2.  Usability  : The user interface should be intuitive,  with easy access to common actions 
like undo/redo. 
3.  Reliability  : Undo and redo actions should accurately  track and reverse all text 
modifications. 
4.  Portability  : The editor should be platform-independent  and run on any system 
supporting Python or other development environments. 
Testing and Validation 
1.  Unit Testing  : 
○  Test insertions and deletions to ensure they modify the text as expected. 
○  Test undo/redo operations for accurate text reversal and reapplication. 
○  Test corner cases (e.g., undo with an empty stack, redo without an undo). 
2.  Performance Testing  : 
○  Measure the performance of the editor with large text inputs and frequent 
undo/redo operations. 
3.  Usability Testing  : 
○  Gather user feedback on the editor's interface and functionality. 
Future Enhancements 
1.  Multiple Documents Support  : Allow users to open and edit multiple documents in 
different tabs. 
2.  Syntax Highlighting  : For developers, syntax highlighting could be added for various 
programming languages. 
3.  Collaboration Feature  : Support real-time collaborative  editing between multiple users. 
4.  Advanced Formatting Options  : Add bold, italic, underline,  and other rich text features. 
5.  Version Control  : Implement versioning to allow users  to revert to older versions of the 
document. 
Conclusion 
This project demonstrates the design and implementation of a basic text editor with the 
undo/redo feature. The use of stacks to manage undo/redo operations ensures efficient and 
effective action reversal. The editor can be enhanced with more advanced features like 
find/replace, save/load, and collaborative editing to increase its usability and appeal. 
