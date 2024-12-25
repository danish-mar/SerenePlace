import os
import datetime

class MoeLogger:
    def __init__(self, file="logs/MoeLogs.logs", version="V0.0.0", error_color=None, warning_color=None, message_color=None, debug=False):
        """
        Initialize the MoeLogger.
        :param file: The file to write logs to.
        :param version: The version of the logger.
        :param error_color: The color for error logs.
        :param warning_color: The color for warning logs.
        :param message_color: The color for general messages.
        :param debug: If True, log messages will be printed to the console.
        """
        self.file = file
        self.version = version
        self.error_color = error_color
        self.warning_color = warning_color
        self.message_color = message_color
        self.debug = debug  # Debug flag to control console output
        self._write_start_header()

    @staticmethod
    def _get_timestamp():
        """
        Get the current timestamp in a readable format.
        :return: A string representing the current timestamp.
        """
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def _write_to_file(self, log_type, text):
        """
        Write a log entry to the specified file with a timestamp.
        If the file doesn't exist, it will be created.
        :param log_type: The type of log (Error, Warning, Message).
        :param text: The log message.
        """
        timestamp = self._get_timestamp()
        with open(self.file, 'a') as log_file:
            log_file.write(f"[{timestamp}] {log_type}: {text}\n")

    def _write_start_header(self):
        """
        Write the start header to the log file.
        """
        with open(self.file, 'a') as log_file:
            log_file.write(f"\n------- {self.version} ---------\n")

    def write_end_header(self):
        """
        Write the end header to the log file when logging ends.
        """
        with open(self.file, 'a') as log_file:
            log_file.write("------- MoeLogger Out -----------\n")

    def warning(self, text):
        """
        Log a warning message with a timestamp.
        :param text: The warning message.
        """
        if self.debug:
            timestamp = self._get_timestamp()
            print(f"⚠️ [{timestamp}] Warning: {text}")
        self._write_to_file("Warning", text)

    def error(self, text):
        """
        Log an error message with a timestamp.
        :param text: The error message.
        """
        if self.debug:
            timestamp = self._get_timestamp()
            print(f"❌ [{timestamp}] Error: {text}")
        self._write_to_file("Error", text)

    def message(self, text):
        """
        Log a general message with a timestamp.
        :param text: The message.
        """
        if self.debug:
            timestamp = self._get_timestamp()
            print(f"✨ [{timestamp}] Message: {text}")
        self._write_to_file("Message", text)

    def character_response(self, text):
        """
        Logs a character Ai response
        :param text: Response from Ai
        """

        if self.debug:
            timestamp = self._get_timestamp()


# Example Usage
if __name__ == "__main__":
    # Set debug flag to True to enable console logging
    debug_mode = True  # Change to False to disable console output
    logger = MoeLogger("moe_log.txt", "v1.0.0", debug=debug_mode)

    logger.warning("This is a warning!")
    logger.error("An error occurred!")
    logger.message("Everything is running smoothly!")

    # Write end header when exiting
    logger.write_end_header()
