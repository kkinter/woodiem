import { VStack, Text } from "@chakra-ui/react";

function Sidebar() {
  return (
    <VStack align="stretch" spacing={4} bg="gold">
      <Text fontWeight="bold">For you</Text>
      <Text fontWeight="bold">Following</Text>
      <Text fontWeight="bold">Django Rest Framework</Text>
      <Text fontWeight="bold">Python</Text>
      <Text fontWeight="bold">Software Engineering</Text>
    </VStack>
  );
}

export default Sidebar;
