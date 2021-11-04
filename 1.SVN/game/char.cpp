// add end

#ifdef ENABLE_DUNGEON_REWARD_SYSTEM
std::tuple<DWORD, BYTE> verlan()
{
	std::vector<std::pair<DWORD,BYTE>> doduller // verilecek itemler bu listeye eklenecek
	//{kod, miktar},
	{
		{70251,10},
		{70252,10},
		{70253,10},
		{70254,10},
		{489,1},
		{3309,1},
		{11219,1},
		{20049,1},
		
	};

	BYTE random = number(0,doduller.size()-1);

	return {doduller[random].first, doduller[random].second};
}

void CHARACTER::ZindanOduluSec(BYTE secilen)
{
	auto [vnum, count] = verlan();

	ChatPacket(CHAT_TYPE_COMMAND, "odulgeldi itemgeldi|%d|%d|%d", secilen, vnum, count); // once cikani gonderiyoruz

	for (BYTE i = 0; i < 4; i++)
	{
		if (i == secilen)
			continue;
		auto [vnum, count] = verlan();
		ChatPacket(CHAT_TYPE_COMMAND, "odulgeldi itemgeldi|%d|%d|%d", i, vnum, count); // geri kalan itemler
	}

	AutoGiveItem(vnum, count); // ver gitsin
}

void CHARACTER::ZindanOdulGuiAc()
{
	ChatPacket(CHAT_TYPE_COMMAND, "odulgeldi guiac|");
}
#endif