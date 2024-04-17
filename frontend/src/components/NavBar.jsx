import {
  Avatar,
  Box,
  Button,
  ButtonGroup,
  Container,
  HStack,
} from "@chakra-ui/react";

const NavBar = () => {
  return (
    <>
      <HStack spacing="10" justifyContent="space-between">
        <ButtonGroup
          size="lg"
          variant="text.accent"
          colorScheme="gray"
          spacing="8"
        >
          <Button>Home</Button>
          <Button>...</Button>
        </ButtonGroup>

        <HStack>
          <Avatar boxSize="10" src="https://i.pravatar.cc/300" />
          <Button size="lg" variant="ghost" colorScheme="gray" spacing="8">
            Login
          </Button>
        </HStack>
      </HStack>
    </>
  );
};

export default NavBar;
