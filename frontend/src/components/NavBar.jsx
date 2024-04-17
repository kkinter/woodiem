import {
  Box,
  Flex,
  Spacer,
  Heading,
  Input,
  IconButton,
  Avatar,
} from "@chakra-ui/react";
import { SearchIcon, BellIcon } from "@chakra-ui/icons";

function NavBar() {
  return (
    <Flex bg="green" p={4} alignItems="center">
      <Box>
        <Heading size="md">Woodiem</Heading>
      </Box>
      <Spacer />
      <Input placeholder="Search" mr={4} />
      <IconButton icon={<SearchIcon />} aria-label="Search" mr={4} />
      <IconButton icon={<BellIcon />} aria-label="Notifications" mr={4} />
      <Avatar name="John Doe" src="https://example.com/avatar.jpg" />
    </Flex>
  );
}

export default NavBar;
