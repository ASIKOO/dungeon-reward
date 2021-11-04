#ifdef ENABLE_DUNGEON_REWARD_SYSTEM
ACMD(do_odulsectim)
{
	if (!ch)
		return;

	char arg1[256];
	one_argument(argument, arg1, sizeof(arg1));

	if (!*arg1)
	{
		ch->ChatPacket(CHAT_TYPE_INFO, "Wrong command use.");
		return;
	}

	BYTE secilen = 0;
	str_to_number(secilen, arg1);

	ch->ZindanOduluSec(secilen);
}
#endif
