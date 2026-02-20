CREATE TABLE `bd-testes`.`user` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `public_id` VARCHAR(45) NOT NULL,
  `name` VARCHAR(100) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `password` VARCHAR(200) NOT NULL,
  `is_active` TINYINT NOT NULL DEFAULT 1,
  PRIMARY KEY (`id`));

INSERT INTO `bd-testes`.`user` (`public_id`, `name`, `email`, `password`) VALUES ('fdb769c0-43b1-452c-9112-344e9f5f457a', 'Tereza Allana Lavínia Almeida', 'terezaallanaalmeida@rafaelmarin.net', '1HK6MZC4xI');
INSERT INTO `bd-testes`.`user` (`public_id`, `name`, `email`, `password`) VALUES ('9d319a1c-d617-43ac-8bed-ecff36b1f7ab', 'Calebe Gustavo Drumond', 'calebe-drumond72@outlock.com', 'fiPF26ujLI');
