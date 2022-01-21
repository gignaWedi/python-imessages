on run {targetBuddyPhone, targetMessage}
	activate application "Messages"
	tell application "System Events" to tell process "Messages"
		key code 45 using command down
		keystroke targetBuddyPhone
		key code 36
		keystroke targetMessage
		key code 36
	end tell
end run
