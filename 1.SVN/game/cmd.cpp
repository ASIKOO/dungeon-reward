#ifdef ENABLE_DUNGEON_REWARD_SYSTEM
ACMD(do_odulsectim);
#endif

// find

	{ "\n",		NULL,			0,			POS_DEAD,	GM_IMPLEMENTOR	}  /* 반드시 이 것이 마지막이어야 한다. */
};

// add over

#ifdef ENABLE_DUNGEON_REWARD_SYSTEM
	{ "odulsectim",	do_odulsectim,	0,	POS_DEAD,	GM_PLAYER	},
#endif