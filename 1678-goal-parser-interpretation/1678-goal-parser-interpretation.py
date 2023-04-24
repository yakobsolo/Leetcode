class Solution:
    def interpret(self, command: str) -> str:
        for _ in range(50):
            command = command.replace('()', "o")
            command = command.replace("(al)", "al")
        return command