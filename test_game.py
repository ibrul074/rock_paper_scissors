import game

def test_npc_choice():
    #check can choose rock, paper, scissors (1,2 and 3)
    for i in range(100):
        npc_choice=game.get_npc_choice()
        if npc_choice == 1:
            break
        # fail if choice is not rock, paper or scissors
        assert npc_choice in [1, 2, 3]
    else:
        raise Exception("npc never chose rock(1)")

    for i in range(100):
        npc_choice=game.get_npc_choice()
        if npc_choice == 2:
            break
        # fail if choice is not rock, paper or scissors
        assert npc_choice in [1, 2, 3]
    else:
        raise Exception("npc never chose paper(2)")

    for i in range(100):
        npc_choice=game.get_npc_choice()
        if npc_choice == 3:
            break
        # fail if choice is not rock, paper or scissors
        assert npc_choice in [1, 2, 3]
    else:
        raise Exception("npc never chose scissors(3)")

def test_convert_choice_to_str():
    assert game.convert_in_str(1) == "rock"
    assert game.convert_in_str(2) == "paper"
    assert game.convert_in_str(3) == "scissors"

def test_determine_who_won():
    assert game.who_won(1,1) == "tie"
    assert game.who_won(2, 2) == "tie"
    assert game.who_won(3, 3) == "tie"
    assert game.who_won(1, 2) == "user"
    assert game.who_won(2, 3) == "user"
    assert game.who_won(3, 1) == "user"
    assert game.who_won(1, 3) == "npc"
    assert game.who_won(2, 1) == "npc"
    assert game.who_won(3, 2) == "npc"

def test_print_who_won_and_choices():
    win_str = game.get_who_won_print_str("user", "paper", "rock")
    assert "won" in win_str

    lose_str = game.get_who_won_print_str("npc", "rock", "paper")
    assert "lose" in lose_str

    tie_str = game.get_who_won_print_str("tie", "rock", "rock")
    assert "tie" in tie_str
