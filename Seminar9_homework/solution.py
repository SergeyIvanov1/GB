from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *





app = ApplicationBuilder().token("5569555207:AAF-ldm3_ZGk4ROs1ZCcjOKOzsTekmreHt4").build()
print("server started")
app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))

app.run_polling()