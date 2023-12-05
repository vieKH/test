from emoji import emojize
import pytest
from test import choices, results, replay_game  # Thay "game_setup" bằng tên thực của module của bạn


@pytest.fixture()
def setup_game():
    computer_choice, user_choice, replay = "", "", ""  # Declaring variables to store choices
    computer_points, user_points, flag, chance = 0, 0, 0, 0  # Variables :
    return computer_points, user_points, flag, chance, computer_choice, user_choice, replay


@pytest.mark.parametrize("user_input, expected_user_choice", [
    ("s", "s"),  # Một trường hợp với input là "s"
    ("w", "w"),  # Một trường hợp với input là "w"
    ("g", "g"),  # Một trường hợp với input là "g"
    ("a", ""),  # Một trường hợp với input không hợp lệ
    # Các trường hợp khác tùy thuộc vào logic của hàm choices
])
def test_choices(monkeypatch, capsys, user_input, expected_user_choice):
    monkeypatch.setattr('builtins.input', lambda _: user_input)  # Giả lập sự nhập vào từ người dùng

    choices()  # Gọi hàm choices

    captured = capsys.readouterr()  # Đọc đầu ra của hàm (stdout và stderr)

    # Kiểm tra xem hàm đã in đúng thông điệp chưa (tùy thuộc vào logic của hàm choices)
    assert "Choose:" in captured.out
    assert f"S for {emojize(':snake:')}" in captured.out
    assert f"W for {emojize(':droplet:')}" in captured.out
    assert f"G for {emojize(':pistol:')}" in captured.out

    # Kiểm tra xem user_choice đã được đặt đúng không
    assert expected_user_choice == input().lower()
