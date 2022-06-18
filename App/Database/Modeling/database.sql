CREATE DATABASE IF NOT EXISTS `rpg_simulator` DEFAULT CHARACTER SET utf8;
USE `rpg_simulator`;

--------------------------
-- Table `rpg_simulator`.`archetype`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `rpg_simulator`.`archetype` (
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(45) NOT NULL,

    PRIMARY KEY (`id`)

) ENGINE = InnoDB;

--------------------------
-- Table `rpg_simulator`.`race`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `rpg_simulator`.`race` (
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(45) NOT NULL,

    PRIMARY KEY (`id`)

) ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `rpg_simulator`.`mount`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `rpg_simulator`.`mount` (
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(45) NULL,
    `level` INT(3) NULL,
    `type` VARCHAR(16) NULL,

    PRIMARY KEY (`id`)

) ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `rpg_simulator`.`weapon`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `rpg_simulator`.`weapon` (
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(30) NULL,
    `type` VARCHAR(20) NULL,
    `level` INT(3) NULL,
    `damage` INT(6) NULL,

    PRIMARY KEY (`id`)

) ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `rpg_simulator`.`character`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `rpg_simulator`.`character` (
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(45) NOT NULL,
	`archetype` VARCHAR(30),
	`race` VARCHAR(30),
    `level` INT UNSIGNED,
    `mount_id` INT UNSIGNED,
    `weapon_id` INT UNSIGNED,

    PRIMARY KEY (`name`),
    
	KEY (`id`),

    CONSTRAINT `fk_mount`
        FOREIGN KEY (`mount_id`)
        REFERENCES `rpg_simulator`.`mount` (`id`)
        ON UPDATE CASCADE
        ON DELETE CASCADE,

    CONSTRAINT `fk_weapon`
        FOREIGN KEY (`weapon_id`)
        REFERENCES `rpg_simulator`.`weapon` (`id`)
        ON UPDATE CASCADE
        ON DELETE CASCADE   

) ENGINE = InnoDB;

-- --------------------------
-- -- Table `rpg_simulator`.`Habilidade_has_Personagem`
-- -- -----------------------------------------------------
-- CREATE TABLE IF NOT EXISTS `rpg_simulator`.`Habilidade_has_Personagem` (
--   `Habilidade_id` INT(11) NOT NULL,
--   `Personagem_id` INT(11) NOT NULL,
--   PRIMARY KEY (`Habilidade_id`, `Personagem_id`),
--   CONSTRAINT `fk_Habilidade_has_Personagem_Habilidade1`
--     FOREIGN KEY (`Habilidade_id`)
--     REFERENCES `rpg_simulator`.`Habilidade` (`id`)
--     ON DELETE NO ACTION
--     ON UPDATE NO ACTION,
--   CONSTRAINT `fk_Habilidade_has_Personagem_Personagem1`
--     FOREIGN KEY (`Personagem_id`)
--     REFERENCES `rpg_simulator`.`Personagem` (`id`)
--     ON DELETE NO ACTION