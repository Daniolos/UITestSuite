import subprocess


class ApplicationManager:
    def __init__(self, command):
        self.command = command
        self.process = None

    def __enter__(self):
        self.process = subprocess.Popen(self.command)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.process:
            self.process.terminate()
            self.process.wait()
