SET time_zone = "+00:00";

CREATE TABLE IF NOT EXISTS `a_pages` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `link` text NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=1001 DEFAULT CHARSET=utf8;

INSERT INTO `a_pages` (`id`, `name`, `link`) VALUES
(1, 'Все сообщения', 'message.php'),
(2, 'Удаленные сообщения', 'del_message.php'),
(3, 'Логи ГС каналов', 'voice.php'),
(999, 'Выход с аккаунта', 'exit.php');

CREATE TABLE IF NOT EXISTS `a_users` (
  `id` int(11) NOT NULL,
  `username` text NOT NULL,
  `password` text NOT NULL,
  `last_join` text NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

INSERT INTO `a_users` (`id`, `username`, `password`, `last_join`) VALUES
(1, 'root', 'root', '');

CREATE TABLE IF NOT EXISTS `delete_messages` (
  `id` int(11) NOT NULL,
  `user_id` text NOT NULL,
  `username` text NOT NULL,
  `message` text NOT NULL,
  `channel` text NOT NULL,
  `time` timestamp NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COMMENT='Логи удаленных сообщений';

INSERT INTO `delete_messages` (`id`, `user_id`, `username`, `message`, `channel`, `time`) VALUES
(14, '1087354143821267017', 'dimenciti', 'проверочка', 'тестирование-бота', '2025-02-06 12:02:06');

CREATE TABLE IF NOT EXISTS `messages` (
  `id` int(11) NOT NULL,
  `user_id` text NOT NULL,
  `username` text NOT NULL,
  `message` text NOT NULL,
  `channel` text NOT NULL,
  `time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB AUTO_INCREMENT=386 DEFAULT CHARSET=utf8mb4 COMMENT='Логи всех сообщений';

INSERT INTO `messages` (`id`, `user_id`, `username`, `message`, `channel`, `time`) VALUES
(1, '1087354143821267017', 'dimenciti', 'еще проверка', '', '2025-01-18 10:12:56'),
(2, '1087354143821267017', 'dimenciti', '*а если с форматом*', '', '2025-01-18 10:13:18')

CREATE TABLE IF NOT EXISTS `message_edit` (
  `user_id` int(11) NOT NULL,
  `username` text NOT NULL,
  `message_original` text NOT NULL,
  `message_edits` text NOT NULL,
  `message_id` text NOT NULL,
  `time` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='Логи измененных сообщений';

CREATE TABLE IF NOT EXISTS `voice_logs` (
  `id` int(11) NOT NULL,
  `user_id` text NOT NULL,
  `username` text NOT NULL,
  `do` text NOT NULL,
  `channel` text NOT NULL,
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

INSERT INTO `voice_logs` (`id`, `user_id`, `username`, `do`, `channel`, `time`) VALUES
(1, '1087354143821267017', 'dimenciti', 'Перемещение', '♨ - Игровая комната -> ♨ - Игровая комната', '2025-02-06 10:55:02'),
(2, '1087354143821267017', 'dimenciti', 'Вход', '🌸 - Мы тут прячемся', '2025-02-06 12:02:15'),
(3, '1087354143821267017', 'dimenciti', 'Выход', '🌸 - Мы тут прячемся', '2025-02-06 12:02:22');

ALTER TABLE `a_pages`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `a_users`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `delete_messages`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `messages`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `voice_logs`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `a_pages`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=1001;

ALTER TABLE `a_users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=2;

ALTER TABLE `delete_messages`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=15;

ALTER TABLE `messages`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=386;

ALTER TABLE `voice_logs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=4;