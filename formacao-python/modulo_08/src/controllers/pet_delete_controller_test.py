from src.controllers.pet_delete_controller import PetDeleteController


def tes_delete_pet(mocker):
    mock_repository = mocker.Mock()
    controller = PetDeleteController(mock_repository)
    controller.delete("Doguinho")

    mock_repository.delete_pets.assert_called_once_with("Doguinho")
