// find:

	void RegisterPCFunctionTable()

// add over:

#ifdef ENABLE_DUNGEON_REWARD_SYSTEM
	ALUA(pc_odul_gui_ac)
	{
		LPCHARACTER ch = CQuestManager::instance().GetCurrentCharacterPtr();
		ch->ZindanOdulGuiAc();
		return 1;
	}
#endif

// if you don't use martysama or don't use ALUA add this

#ifdef ENABLE_DUNGEON_REWARD_SYSTEM
	int pc_odul_gui_ac(lua_State* L)
	{
		LPCHARACTER ch = CQuestManager::instance().GetCurrentCharacterPtr();
		ch->ZindanOdulGuiAc();
		return 1;
	}
#endif



// find:

			{ NULL,			NULL			}
		};

// add over:

#ifdef ENABLE_DUNGEON_REWARD_SYSTEM
			{ "open_dr_gui",				pc_odul_gui_ac		},
#endif