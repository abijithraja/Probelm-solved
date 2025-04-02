import java.util.Stack;

class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        
        // Traverse through the string
        for (char c : s.toCharArray()) {
            // Push opening brackets onto the stack
            if (c == '(' || c == '{' || c == '[') {
                stack.push(c);
            }
            // Check if the stack is not empty and the top of the stack matches the closing bracket
            else if (c == ')' && !stack.isEmpty() && stack.peek() == '(') {
                stack.pop();  // Pop the matching opening bracket
            }
            else if (c == '}' && !stack.isEmpty() && stack.peek() == '{') {
                stack.pop();  // Pop the matching opening bracket
            }
            else if (c == ']' && !stack.isEmpty() && stack.peek() == '[') {
                stack.pop();  // Pop the matching opening bracket
            } else {
                return false;  // Invalid if no matching opening bracket
            }
        }
        
        // If the stack is empty, all brackets matched correctly
        return stack.isEmpty();
    }
}
