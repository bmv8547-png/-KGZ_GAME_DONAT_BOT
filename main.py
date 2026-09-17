@dp.callback_query(F.data == "price")
async def show_price(callback: types.CallbackQuery):
    text = (
        "⚠️ **Цены для гильдия боты:**\n\n"
        "• 4 бот — 180 сом ✅\n"
        "• 8 бот — 370 сом ✅\n"
        "• 12 бот — 560 сом ✅\n"
        "• 16 бот — 750 сом ✅\n"
        "• 20 бот — 945 сом ✅\n\n"
        "_Все это временно_\n\n"
        "💎 **Алмазы:**\n"
        "• 90-110 алмаз\n"
        "• 270-341 алмаз\n"
        "• 410-572 алмаз\n"
        "• 800-1166 алмаз\n"
        "• 1600-2398 алмаз\n"
        "• 3900-6150 алмаз\n"
        "• Недельный ваучер — 165 сом\n"
        "• Недельный лайт ваучер — 40 сом"
    )
    await callback.message.answer(text, parse_mode="Markdown")
    await callback.answer()


@dp.callback_query(F.data == "donat")
async def process_donat(callback: types.CallbackQuery):
    text = (
        "💳 **Төлөм реквизиттери:**\n\n"
        "OBANK / BAKAIBANK: `0700341671`\n\n"
        "Төлөгөндөн кийин чекти жана оюндагы ID'ңизди админге жөнөтүңүз!"
    )
    await callback.message.answer(text, parse_mode="Markdown")
    await callback.answer()
    
